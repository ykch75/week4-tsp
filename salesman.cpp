#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <math.h>
#include <limits>
using namespace std;
const double INF = 99999999.99;
const int def = 2048;

void input(int);
void twoOpt(vector<int>,vector<vector<double>   > ,int);
void move();
void solve();

struct point {
    double x;
    double y;
};

double distance(point city1,point city2){
    double dist=sqrt((city1.x-city2.x)*(city1.x-city2.x)+(city1.y-city2.y)*(city1.y-city2.y));
    return dist;
}

vector<string> split(string& input, char delimiter)
{
    istringstream stream(input);
    string field;
    vector<string> result;
    while (getline(stream, field, delimiter)) {
        result.push_back(field);
    }
    return result;
}

void move(vector<vector<double>   > dist,int num){
    int curCity=0,min,i;
    double minKeiro;
    vector<int> unCity(num-1);
    vector<vector<double>   > basicD(num,vector<double>(num));

    for(int i=0;i<num-1;i++) unCity[i]=i+1;
    vector<int> keiro(num);
    vector<int> tour;
    tour.push_back(curCity);
    int nextCity;

    for(int j=0;j<num-1;j++){
        double min_dist=INF;
        for(i=0;i<num-1;i++){
            if((min_dist>dist[curCity][unCity[i]])&&(curCity!=unCity[i])){
                nextCity=unCity[i];
                min_dist=dist[curCity][unCity[i]];
            }
            basicD[curCity][i]=min_dist;
        }
        for(i=0;i<num;i++) dist[curCity][i]=dist[i][curCity]=INF;
        tour.push_back(nextCity);
        curCity = nextCity;
    }
    for(int i=0;i<num;i++) input(tour[i]);
    double total=0;
    for(int i=0;i<num-1;i++) {
        total+=basicD[tour[i]][tour[i+1]];
    }
    printf("path:%lf\n",total);
}
/*
void twoOpt(vector<int> tour,vector<vector<double>   > dist,int num){
    for(int i=0;i<num;i++){
        for(int j=0;j<num;j++){
            if(dist[tour[i]][tour[i+1]]>dist[tour[j]][tour[j+1]]){
                swap(tour[i],tour[j]);
            }
        }
    }
    for(int i=0;i<num;i++) input(tour[i]);
}*/

//ファイルに書き込む
void input(int i){
    string filename = "solution_yours_6.csv";
    ofstream writing_file;
    writing_file.open(filename,ios::app);
    writing_file << i << endl;
}

void solve(point city[],int num){
    vector<vector<double>   > dist(num,vector<double>(num));
    //二点間の距離
    for(int j=0;j<num;j++){
        for(int k=0;k<num;k++){
            dist.at(j).at(k)=distance(city[j],city[k]);
        }
    } 
    move(dist,num);
}

int main(int argc,char* argv[]){
    ifstream fin(argv[1]);//ファイルを開く
    string str;
    remove("solution_yours_6.csv");
    //ファイルの初期化
    struct point city[def];
    int num=0;

	//エラー処理
	if(fin.fail()){
		cerr << "Error: file not opened." << endl;
		return (0);
	}
    getline(fin,str);//1行目を捨てる
    vector<string> strvec;
    while(getline(fin,str)){
        strvec = split(str,',');
        city[num].x=stof(strvec.at(0));
        city[num].y=stof(strvec.at(1));
        num++;
    }
    solve(city,num);

	fin.close();
    return 0;
}