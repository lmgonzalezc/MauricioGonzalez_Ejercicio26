#include <iostream>
#include <fstream>
using namespace std;


void solve_equation_euler(float t_init, float t_end, float delta_t, float omega, string filename);
void solve_equation_rk4(float t_init, float t_end, float delta_t, float omega, string filename);
void solve_equation_leapfrog(float t_init, float t_end, float delta_t, float omega, string filename);

float dzdt(float t, float y, float z, float omega);
float dydt(float t, float y, float z, float omega);

int main(){
  float omega=1.0;
  solve_equation_euler(0.0, 10000.0, omega/2, omega, "euler.dat");
  solve_equation_rk4(0.0, 10000.0, omega/2, omega, "rk4.dat");
  solve_equation_leapfrog(0.0, 10000.0, omega/2, omega, "leapfrog.dat");
  return 0;
}
void solve_equation_euler(float t_init, float t_end, float delta_t, float omega, string filename){
    float t=t_init;
    float y=1.0;
    ofstream outfile;
    outfile.open(filename);

    while(t<t_end){    
        outfile << t << " " << y << endl;
        y = y - delta_t * omega  * y;
        t = t + delta_t;
    }
    outfile.close();
}
void solve_equation_rk4(float t_init, float t_end, float delta_t, float omega, string filename){
    ofstream outfile;
    outfile.open(filename);
    
    
    outfile.close();    
}
void solve_equation_leapfrog(float t_init, float t_end, float delta_t, float omega, string filename){
    float t = t_init;
    float y=1.0;
    float v=0.0;
    ofstream outfile;
    outfile.open(filename);
    
    while(t<t_end){    
        outfile << t << " " << y << endl;
        v = v + -omega * omega * y * (delta_t/2);
        y = y + v * delta_t;
        v = v + -omega * omega * y * (delta_t/2);
    }
    outfile.close();    
}
