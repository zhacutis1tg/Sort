#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <chrono>
#include <iomanip>
#include <string>
#include <numeric>

using namespace std;
using namespace std::chrono;

template <typename T>
vector<T> load_data(string filename) {
    ifstream file(filename, ios::binary);
    file.seekg(0, ios::end);
    streampos fileSize = file.tellg();
    file.seekg(0, ios::beg);
    vector<T> vec(fileSize / sizeof(T));
    file.read(reinterpret_cast<char*>(vec.data()), fileSize);
    return vec;
}

template <typename T>
double benchmark(string name, string filepath) {
    vector<T> arr = load_data<T>(filepath);

    if (arr.empty()) return -1.0;

    auto start = high_resolution_clock::now();
    sort(arr.begin(), arr.end());
    auto stop = high_resolution_clock::now();

    duration<double, std::milli> ms_double = stop - start;

    double ms = ms_double.count();

    cout << left << setw(15) << name << " | " << fixed << setprecision(2) << setw(10) << ms << " ms" << endl;

    return ms;
}

int main() {
    string path = "cpp_data/";
    vector<double> times;
    double t;

    if((t = benchmark<double>("asc",    path + "asc.bin"))   != -1.0) times.push_back(t);
    if((t = benchmark<double>("desc",   path + "desc.bin"))  != -1.0) times.push_back(t);
    if((t = benchmark<double>("rand1",  path + "rand1.bin")) != -1.0) times.push_back(t);
    if((t = benchmark<double>("rand2",  path + "rand2.bin")) != -1.0) times.push_back(t);
    if((t = benchmark<double>("rand3",  path + "rand3.bin")) != -1.0) times.push_back(t);

    if((t = benchmark<long long>("rand4", path + "rand4.bin")) != -1.0) times.push_back(t);
    if((t = benchmark<long long>("rand5", path + "rand5.bin")) != -1.0) times.push_back(t);
    if((t = benchmark<long long>("rand6", path + "rand6.bin")) != -1.0) times.push_back(t);
    if((t = benchmark<long long>("rand7", path + "rand7.bin")) != -1.0) times.push_back(t);
    if((t = benchmark<long long>("rand8", path + "rand8.bin")) != -1.0) times.push_back(t);

    cout << "-----------------------------------" << endl;
    double total = 0;
    for (double time : times) {
        total += time;
    }
    double avg = total / times.size();
    cout << left << setw(15) << "TRUNG BINH: " << fixed << setprecision(2) << avg << " ms" << endl;

    return 0;
}
