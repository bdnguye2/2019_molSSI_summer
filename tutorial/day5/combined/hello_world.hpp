/* This is a header file with .hpp extension but, not needed. Also,
it is a good place for doxygen aka documentation
*/

#pragma once

double f_to_celsius(double f_temp);

double cel_to_kelvin(double c_temp);

double f_to_kelvin(double f_temp);

// Returns false if f_temp is unphysical
bool check_temperature(double f_temp);

void count(int max);
