#include <iostream>
#include <iomanip>
#include <chrono> 
#include <vector>
#include <algorithm>

using namespace std;


double relativeError(double error_value,double real_value){
    return abs((error_value - real_value)/real_value);
}

double absoluteError(double error_value, double real_value){
    return abs(error_value - real_value);
}

float sumFloat(float arr[],int N){
    float sum = 0;
    for(int i =0; i < N;i++){
        sum+=arr[i];
    }
    return sum;
}

vector<float> sumFloatPlot(float arr[],int N,int interval){
    //only generates a vector, doesnt actaully plot the values
    float sum = 0;
    vector<float> relativeErrorValues;
    int k = 0;
    for(int i = 0;i<N;i++){
        sum+=arr[i];
        if(i%interval == 0){
            relativeErrorValues.push_back(relativeError(sum,arr[i]*(i+1))); 
            k++;
        }
    }
    return relativeErrorValues;

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
    float v = 0.53125f;
    const float badCaseValue = 0.333333f;
    
    for(int i = 0; i < N;i++){
        arr[i] = v;
    }

    
    float realValue = N*v;
    float sum = sumFloat(arr,N); //regular sum value
    float recSum = recursiveSum(arr,0,N-1); //recursive sum value 
    float kahanSum = kahanAlgorithm(arr,N); //kahan algorithm sum value

    
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


    //bad case for recursive sum algorithm 
    const int badCaseArraySize = 10000000;
    float *badCaseArray = new float[badCaseArraySize];
    for(int i =0;i<badCaseArraySize;i++){
        badCaseArray[i] = badCaseValue;
    }
   

    float badCaseRecSum = recursiveSum(badCaseArray,0,badCaseArraySize-1);
    float badCaseArrayRealValue = badCaseValue*badCaseArraySize;



    cout << "Absolute error recursive sum for sorted array: " << setprecision(10) << absoluteError(badCaseRecSum,badCaseArrayRealValue) << endl;
    cout << "Relative error recursive sum for sorted array: " << setprecision(10) << relativeError(badCaseRecSum,badCaseArrayRealValue) << endl;


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


    //creating array of relative error values used to plot the error
    //the plot is plotted outside of this code
    auto plot = sumFloatPlot(arr,N,25000);
   
   

    delete(arr);
    delete(badCaseArray);
}