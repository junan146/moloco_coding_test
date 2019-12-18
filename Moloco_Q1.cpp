#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;
bool equalsWhenOneCharRemoved(string x, string y) { 
    int i=0, j=0;
    bool alreadyRemoved = false;
    int size_x=x.size();
    int size_y=y.size();
    bool res = true;
    
    if(abs(size_x-size_y)!=1) return false;
    else{
        while(i<size_x&&j<size_y){
            if(x[i]!=y[j]){
                if(alreadyRemoved) return false;
                if(x[i+1]==y[j]){
                    i++;
                    alreadyRemoved = true;
                }
                else if(x[i]==y[j+1]){
                    j++;
                    alreadyRemoved = true;
                }
                else return false;
            }
            i++;
            j++;
        }
    }
    return res; 
}

int main(){
    string x,y;
    cin>>x>>y;

    cout<<equalsWhenOneCharRemoved(x,y)<<endl;
   
}
