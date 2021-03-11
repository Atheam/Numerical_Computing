#include <iostream>
#include <iomanip>
#include <chrono> 

using namespace std;




float sumFloat(float arr[],int N){
    float sum = 0;
    for(int i =0; i < N;i++){
        sum+=arr[i];
    }
    return sum;
}

float relativeError(float error_value,float real_value){
    return abs((error_value - real_value)/real_value);
}

float absoluteError(float error_value, float real_value){
    return abs(error_value - real_value);
}


float recursiveSum(float arr[], int left, int right)
{
    if (left == right)
    {
        return arr[left];
    }
    int mid = (left+right)/2;
    return recursiveSum(arr,left,mid) + recursiveSum(arr,mid+1,right);

}

float kahanAlgorithm(float arr[],int N){
    float sum = 0.0f;
    float err = 0.0f;
    for(int i = 0;i < N;i++){
        float y =arr[i] - err;
        float temp = sum +y;
        err = (temp - sum) -y;
        sum = temp;
    }
    return sum;
}



int main(){
    const int N = 10000000;
    float *arr = new float[N];
    float v = 0.53125;
    for(int i = 0; i < N;i++){
        arr[i] = v;
    }

    float sum = sumFloat(arr,N);
    float realValue = N*v;
    float recSum = recursiveSum(arr,0,N);
    float kahanSum = kahanAlgorithm(arr,N);

    
    cout << "Real value: " << setprecision(10) << realValue << endl;

    cout << "Sum N elements: " << setprecision(10) << sum << endl;
    cout << endl;

    cout << "Absolute error: " << setprecision(10) << absoluteError(sum,realValue) << endl;
    
    cout << "Relative error: " << setprecision(10) << relativeError(sum,realValue) << endl;

    cout << endl;

    cout << "Recursive sum: " << setprecision(10) <<  recSum << endl;

    cout << "Absolute error recursive sum: " << setprecision(10) << absoluteError(recSum,realValue) << endl;

    cout << "Relative error recursive sum: " << setprecision(10) << relativeError(recSum,realValue) << endl;

    cout << endl;



    auto start = std::chrono::high_resolution_clock::now();  
    sumFloat(arr,N);
    auto stop = std::chrono::high_resolution_clock::now(); 
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);

    cout << "Regular sum time: " << duration.count() << " microseconds" << endl; 



    start = std::chrono::high_resolution_clock::now(); 
    recursiveSum(arr,0,N);
    stop = std::chrono::high_resolution_clock::now(); 
    duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);

    cout << "Recursive sum time: " << duration.count() << " microseconds"<< endl; 

    start = std::chrono::high_resolution_clock::now(); 
    kahanAlgorithm(arr,N);
    stop = std::chrono::high_resolution_clock::now(); 
    duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);

    cout << "Kahan algorithm sum time: " << duration.count() << " microseconds"<< endl; 

    cout << endl;

    cout << "Kahan algorithm sum: " << setprecision(10) << kahanSum << endl;

    cout << "Absolute error kahan algorithm: " << setprecision(10) << absoluteError(kahanSum,realValue) << endl;

    cout << "Relative error kahan algorithm: " << setprecision(10) << relativeError(kahanSum,realValue) << endl;




}