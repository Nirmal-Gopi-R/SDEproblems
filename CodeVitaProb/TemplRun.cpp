#include<bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
        cin>>arr[i];
    int m;
    cin>>m;
    while(m--)
    {
        int sum=0;
        int target;
        cin>>target;
        int f=-1;
        for(int i=0;i<n;i++)
        {
            sum+=arr[i];
            if(sum>=target)
            {
                f=i+1;
                break;
            }
        }
        cout<<f<<"\n";
    }
    return 0;
}
