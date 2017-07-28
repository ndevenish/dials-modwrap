project(annlib_adaptbx)

add_library( annlib_adaptbx INTERFACE )
target_include_directories(annlib_adaptbx INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/include ${CMAKE_BINARY_DIR}/annlib_adaptbx/include/)

add_libtbx_refresh_command( ${CMAKE_CURRENT_SOURCE_DIR}/libtbx_refresh.py
     OUTPUT ${CMAKE_BINARY_DIR}/annlib_adaptbx/include/ANNSELF_INCLUDE/ANN.h
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/include/ANNSELF_INCLUDE/ANNperf.h
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/include/ANNSELF_INCLUDE/ANNx.h
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/ANN.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/bd_fix_rad_search.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/bd_pr_search.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/bd_search.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/bd_tree.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/bd_tree.h
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/brute.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_dump.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_fix_rad_search.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_fix_rad_search.h
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_pr_search.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_pr_search.h
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_search.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_search.h
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_split.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_split.h
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_tree.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_tree.h
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_util.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/kd_util.h
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/perf.cpp
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/pr_queue.h
            ${CMAKE_BINARY_DIR}/annlib_adaptbx/self_include/pr_queue_k.h )

add_subdirectory(ann)
