project(scitbx)

add_library( scitbx INTERFACE )
target_include_directories(scitbx INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_libtbx_refresh_command( ${CMAKE_CURRENT_SOURCE_DIR}/libtbx_refresh.py
     OUTPUT ${CMAKE_BINARY_DIR}/include/scitbx/array_family/detail/operator_functors.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/detail/std_imports.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/operator_traits_builtin.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/ref_algebra.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/ref_apply.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/shared_algebra.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/shared_apply.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/shared_plain_apply.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/shared_reductions.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/small_algebra.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/small_apply.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/small_plain_apply.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/small_reductions.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/tiny_algebra.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/tiny_apply.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/tiny_plain_apply.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/tiny_reductions.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/versa_algebra.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/versa_apply.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/versa_plain_apply.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/versa_reductions.h
            ${CMAKE_BINARY_DIR}/include/scitbx/array_family/boost_python/flex_fwd.h
            ${CMAKE_BINARY_DIR}/include/scitbx/lbfgs_fem.hpp
            ${CMAKE_BINARY_DIR}/scitbx/lbfgs/lbfgs_fem.cpp
            ${CMAKE_BINARY_DIR}/scitbx/lbfgs/sdrive_fem.cpp )

add_library ( scitbx_boost_python 
            boost_python/utils.cpp
            boost_python/slice.cpp
            array_family/boost_python/utils.cpp )
target_link_libraries(scitbx_boost_python Boost::python scitbx)

add_python_library ( scitbx_cubicle_neighbors_ext
            cubicle_neighbors_ext.cpp )
target_link_libraries(scitbx_cubicle_neighbors_ext scitbx_boost_python)

add_python_library ( scitbx_r3_utils_ext
            r3_utils_ext.cpp )
target_link_libraries(scitbx_r3_utils_ext scitbx_boost_python)

add_subdirectory(array_family)
add_subdirectory(error)
add_subdirectory(examples)
add_subdirectory(fftpack)
add_subdirectory(glmtbx)
add_subdirectory(graphics_utils)
add_subdirectory(iso_surface)
add_subdirectory(lbfgs)
add_subdirectory(lbfgsb)
add_subdirectory(linalg)
add_subdirectory(lstbx)
add_subdirectory(math)
add_subdirectory(matrix)
add_subdirectory(minpack)
add_subdirectory(random)
add_subdirectory(rigid_body)
add_subdirectory(serialization)
add_subdirectory(slatec)
add_subdirectory(sparse)
add_subdirectory(stl)
add_subdirectory(suffixtree)
add_subdirectory(wigner)
