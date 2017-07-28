add_executable(tst_cholesky tst_cholesky.cpp)
add_test(NAME tst_cholesky COMMAND tst_cholesky)

add_executable(tst_givens tst_givens.cpp)
add_test(NAME tst_givens COMMAND tst_givens)

add_executable(tst_householder tst_householder.cpp)
add_test(NAME tst_householder COMMAND tst_householder)

add_executable(tst_svd tst_svd.cpp)
add_test(NAME tst_svd COMMAND tst_svd)

