#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){

    cout <<"Hello WOrld!"<<endl;
    string kek = "My string";
    cout << kek.length()<<endl;

    vector<int> a = {1,2,3,4,5};

    for (int i = 0; i < a.size(); i++){
        cout << a[i]<<endl;
    }

    for (auto i : a){
        cout << i<<endl;
    }

    return 0;
}