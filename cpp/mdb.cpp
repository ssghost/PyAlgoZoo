#include <complex>
#include <fstream>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

class MandelbrotSet {
 public:
  std::vector<int> image;  
  int WIDTH;               
  int HEIGHT;              

  double REAL_MIN = -2;    
  double REAL_MAX = 2;     
  double IMAG_MIN = -1.5;  
  double IMAG_MAX = 1.5;   

  const int MAX_ITER;  

  MandelbrotSet(int width, int height, int maxIter, int numThreads)
      : WIDTH(width),
        HEIGHT(height),
        MAX_ITER(maxIter),
        NUM_THREADS(numThreads) {
    image.resize(WIDTH * HEIGHT);
  }

  void renderFractal() {
    std::vector<std::thread> threads;
    int rowsPerThread = HEIGHT / NUM_THREADS;

    for (int i = 0; i < NUM_THREADS; ++i) {
      int startRow = i * rowsPerThread;
      int endRow = (i == NUM_THREADS - 1) ? HEIGHT : (i + 1) * rowsPerThread;
      threads.push_back(std::thread(&MandelbrotSet::renderFractalPart, this,
                                    startRow, endRow));
    }

    for (auto& thread : threads) {
      thread.join();
    }
  }

 private:
  int NUM_THREADS;  

  void renderFractalPart(int startRow, int endRow) {
    for (int y = startRow; y < endRow; ++y) {
      for (int x = 0; x < WIDTH; ++x) {
        double realPart = REAL_MIN + (REAL_MAX - REAL_MIN) * x / WIDTH;
        double imagPart = IMAG_MIN + (IMAG_MAX - IMAG_MIN) * y / HEIGHT;
        std::complex<double> c(realPart, imagPart);
        std::complex<double> z = 0;
        int iter = 0;

        while (std::abs(z) <= 2 && iter < MAX_ITER) {
          z = z * z + c;
          iter++;
        }

        image[y * WIDTH + x] = iter;  
      }
    }
  }
};
