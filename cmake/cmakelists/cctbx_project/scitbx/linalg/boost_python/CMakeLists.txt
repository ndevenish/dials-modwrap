add_python_library ( scitbx_linalg_ext
            linalg_ext.cpp
            matrix.cpp
            cholesky.cpp
            householder.cpp
            svd.cpp
            eigensystem.cpp
            lapack_fem_bpl.cpp )
target_link_libraries(scitbx_linalg_ext scitbx_boost_python)

