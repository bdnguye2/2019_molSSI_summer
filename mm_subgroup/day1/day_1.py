import numpy as np
import time

def generate_initial_state(method='random', file_name=None, num_particles=None,
                           box_length=None):
    # Generates initial coordinates
    if method is 'random':
        # Coordinates centered within the box
        coordinates = (0.5 - np.random.rand(num_particles, 3))*box_length
        
    elif method is 'file':
        # Reads in a file with the reference coordinates
        coordinates = np.loadtxt(file_name,skiprows=2,usecols=(1,2,3))
        
    return coordinates

def lennard_jones_potential(rij2):
    sig_by_r6 = np.power(1/rij2, 3)
    sig_by_r12 = np.power(sig_by_r6, 2)
    return 4.0*(sig_by_r12 - sig_by_r6)

def calculate_tail_correction(box_length, cutoff, number_particles):
    # Provides the standard tail energy correction for LJ potential
    sig_by_cutoff3 = np.power(1/cutoff, 3)
    sig_by_cutoff9 = np.power(sig_by_cutoff3, 3)
    return (8.0*np.pi*(number_particles)**2.)/(3.*box_length**3.)*((1./3.)*sig_by_cutoff9
                                                                   - sig_by_cutoff3)

def minimum_image_distance(r_i, r_j, box_length):
    # Computes minimum image distance between two particles
    rij = r_i - r_j
    rij = rij - box_length*np.round(rij/box_length)
    rij2 = np.dot(rij, rij)
    return rij2

def get_particle_energy(coordinates, box_length, i_particle, cutoff2):
    # Compute the energy of particle with the rest of the system
    e_total = 0.0
    i_position = coordinates[i_particle]
    particle_count = len(coordinates)
    
    for j_particle in range(particle_count):
        if i_particle != j_particle:
            j_position = coordinates[j_particle]
            rij2 = minimum_image_distance(i_position, j_position, box_length)

            if rij2 < cutoff2:
                e_pair = lennard_jones_potential(rij2)
                e_total += e_pair

    return e_total

def calculate_total_pair_energy(coordinates, box_length, cutoff2):
    # cutoff2 is the square of the cutoff radius
    e_total = 0.0
    particle_count = len(coordinates)

    # For loop prevents double counting
    for i_particle in range(particle_count):
        for j_particle in range(i_particle):
            r_i = coordinates[i_particle]
            r_j = coordinates[j_particle]
            rij2 = minimum_image_distance(r_i, r_j, box_length)
            if rij2 < cutoff2:
                e_pair = lennard_jones_potential(rij2)
                e_total += e_pair
    return e_total

def accept_or_reject(delta_e, beta):
    # Accepts or rejects a move given the energy difference and system temperature
    if delta_e < 0.0:
        accept = True

    else:
        random_number = np.random.rand(1)
        p_acc = np.exp(-beta*delta_e)

        if random_number < p_acc:
            accept = True
        else:
            accept = False

    return accept

def adjust_displacement(n_trails, n_accept, max_displacement):
    # Acceptance rate is adjusted depending whether too much or too little
    acc_rate = float(n_accept)/float(n_trials)
    if (acc_rate < 0.38):
        max_displacement *= 0.8

    elif (acc_rate > 0.42):
        max_displacement *= 1.2

    return max_displacement

#Checking the first configuration of the 800 Argon atoms in a 10x10x10 box
#coordinates = generate_initial_state(method='file', file_name='sample_config1.xyz')
#print(calculate_total_pair_energy(coordinates, 10.0, 9)) #<- cutoff squared
#print(calculate_tail_correction(10.0,3.0,800))

#---------------------------------------------------------------------------------
# Parameters Setup
#---------------------------------------------------------------------------------

reduced_temperature = 0.9
reduced_density = 0.9
n_steps = 50000
freq = 1000
num_particles = 100
simulation_cutoff = 3.0
max_displacement = 0.1
tune_displacement = True
build_method = 'random'

box_length = np.cbrt(num_particles/reduced_density)
beta = 1.0/reduced_temperature
simulation_cutoff2 = np.power(simulation_cutoff, 2)

# Tracks the number of accepted trials
n_trials = 0
n_accept = 0
energy_array = np.zeros(n_steps)

#---------------------------------------------------------------------------------
# Metropolis Monte Carlo Simulation
#---------------------------------------------------------------------------------

coordinates = generate_initial_state(method=build_method, num_particles=num_particles,
                                     box_length=box_length)

# Initial pair_energy and tail_correction
total_pair_energy = calculate_total_pair_energy(coordinates, box_length, simulation_cutoff2)
tail_correction = calculate_tail_correction(box_length, simulation_cutoff, num_particles)

# For loop simulation
for i_step in range(n_steps):
    n_trials += 1
    i_particle = np.random.randint(num_particles)
    random_displacement = (2.0*np.random.rand(3) - 1.0)*max_displacement
    
    # Recompute the current energy
    current_energy = get_particle_energy(coordinates, box_length, i_particle, simulation_cutoff2)

    # Proposed coordinates displacement
    proposed_coordinates = coordinates.copy()
    proposed_coordinates[i_particle] += random_displacement
    proposed_energy = get_particle_energy(proposed_coordinates, box_length, i_particle,
                                          simulation_cutoff2)

    delta_e = proposed_energy - current_energy

    accept = accept_or_reject(delta_e, beta)

    if accept:
        total_pair_energy += delta_e
        n_accept += 1
        coordinates[i_particle] += random_displacement

    # Final Energy and array of the energy at each step for plotting
    total_energy = (total_pair_energy + tail_correction)/num_particles
    energy_array[i_step] = total_energy

    if np.mod(i_step + 1, freq) == 0:
        print(i_step + 1, energy_array[i_step])
        if tune_displacement:
            max_displacement = adjust_displacement(n_trials, n_accept,max_displacement)
