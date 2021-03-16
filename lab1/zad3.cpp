#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

float riemannSum(int n, float s){
    float sum = 0;
    for(float k = 1;k <= n;k++){

        sum+=1.0/pow(k,s);
    }
    return sum;
}

float dirichletSum(int n,float s){
    float sum = 0;
    for(float k = 1; k <= n;k++){
        sum+=pow(-1.0,k-1.0) / pow(k,s);
    }
    return sum;
}

float riemannSumBackwards(int n, float s){
    float sum = 0;
    for(float k = n;k >= 1;k--){
        sum+=1.0/pow(k,s);
    }
    return sum;
}

float dirichletSumBackwards(int n,float s){
    float sum = 0;
    for(float k = n; k >= 1;k--){
        sum+=pow(-1.0,k-1.0) / pow(k,s);
    }
    return sum;
}



float riemannSumDouble(int n, double s){
    double sum = 0;
    for(double k = 1;k <= n;k++){

        sum+=1.0/pow(k,s);
    }
    return sum;
}



float dirichletSumDouble(int n,double s){
    double sum = 0;
    for(double k = 1; k <= n;k++){
        sum+=pow(-1.0,k-1.0) / pow(k,s);
    }
    return sum;
}

float riemannSumDoubleBackwards(int n, double s){
    double sum = 0;
    for(double k = n;k >= 1;k--){
        sum+=1.0/pow(k,s);
    }
    return sum;
}

float dirichletSumDoubleBackwards(int n,double s){
    double sum = 0;
    for(double k = n; k >= 1;k--){
        sum+=pow(-1.0,k-1.0) / pow(k,s);
    }
    return sum;
}






int main(){
    int N = 5;
    int n[] = {50,100,200,500,1000};
    float s[] = {2,3.6667,5,7.2,10};



    cout << "SUM FORWARD USING FLOAT" << endl;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout << "n = " << n[i] << " s = " << s[j] << " Riemann zeta function sum forward, float: " 
            << setprecision(10) << riemannSum(n[i],s[j]) << endl;
            cout << "n = " << n[i] << " s = " << s[j] << " Dirichlet eta function sum forward, float: " 
            << setprecision(10) << dirichletSum(n[i],s[j]) << endl;
            cout << endl;
        }
        cout << endl << endl;
    }

    cout << "SUM BACKWARDS USING FLOAT" << endl << endl;


     for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout << "n = " << n[i] << " s = " << s[j] << " Riemann zeta function sum backwards, float: " 
            << setprecision(10) << riemannSumBackwards(n[i],s[j]) << endl;
            cout << "n = " << n[i] << " s = " << s[j] << " Dirichlet eta function sum backwards, float: " 
            << setprecision(10) << dirichletSumBackwards(n[i],s[j]) << endl;
            cout << endl;
        }
        cout << endl << endl << endl;
    }


    double s_double[] = {2,3.6667,5,7.2,10};


    cout << "SUM FORWARD USING DOUBLE" << endl;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout << "n = " << n[i] << " s = " << s_double[j] << " Riemann zeta function sum forward, double: " 
            << setprecision(10) << riemannSumDouble(n[i],s_double[j]) << endl;
            cout << "n = " << n[i] << " s = " << s_double[j] << " DIrichlet eta function sum forward, double : " 
            << setprecision(10) << dirichletSumDouble(n[i],s_double[j]) << endl;
            cout << endl;
        }
        cout << endl << endl;
    }


    cout << "SUM BACKWARDS USING DOUBLE" << endl;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout << "n = " << n[i] << " s = " << s_double[j] << " Riemann zeta function sum backwards, double: " 
            << setprecision(10) << riemannSumDoubleBackwards(n[i],s_double[j]) << endl;
            cout << "n = " << n[i] << " s = " << s_double[j] <<  " Dirichlet eta function sum backwards, float: " 
            << setprecision(10) << dirichletSumDoubleBackwards(n[i],s_double[j]) << endl;
            cout << endl;
        }
        cout << endl << endl;
    }



   





}