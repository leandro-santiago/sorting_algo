#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
#include <vector>

namespace py = pybind11;
using namespace std;

PYBIND11_MAKE_OPAQUE(vector<string>);

int partition(vector<string> & list, int low, int up) {
  int center = (up - low) >> 1; // (up - low) / 2
  string pivot = list[low + center];
  int i = low;
  int j = up;
  string aux = "";

  while (true) {
    while (list[i] < pivot) {
      i++;
    }

    while (list[j] > pivot) {
      j--;
    }

    if (i >= j) return j;

    aux = list[i];
    list[i] = list[j];
    list[j] = aux;
  }  
}

void _quicksort(vector<string> & list, int low, int up) {
  if (low < up) {
    int pivot = partition(list, low, up);
    _quicksort(list, low, pivot);
    _quicksort(list, pivot + 1, up);
  }
} 

void quicksort(vector<string> & list) {
  _quicksort(list, 0, list.size() - 1);
}

PYBIND11_MODULE(csort, m) {
  py::bind_vector<vector<string>>(m, "VectorString", py::module_local(false))
    .def("quicksort", &quicksort); 
}

