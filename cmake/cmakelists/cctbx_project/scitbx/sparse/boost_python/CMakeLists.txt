add_python_library ( scitbx_sparse_ext
            vector.cpp
            matrix.cpp
            approx_equal.cpp
            random.cpp
            lu_factorization.cpp
            sparse_ext.cpp )
target_link_libraries(scitbx_sparse_ext scitbx_boost_python)

