project(annlib)

add_library( annlib INTERFACE )
target_include_directories(annlib INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/include)

add_library ( ann 
            src/ANN.cpp
            src/bd_fix_rad_search.cpp
            src/bd_pr_search.cpp
            src/bd_search.cpp
            src/bd_tree.cpp
            src/brute.cpp
            src/kd_dump.cpp
            src/kd_fix_rad_search.cpp
            src/kd_pr_search.cpp
            src/kd_search.cpp
            src/kd_split.cpp
            src/kd_tree.cpp
            src/kd_util.cpp
            src/perf.cpp
            ../annlib_adaptbx/ann/ann_adaptor.cpp )
add_generated_sources(ann
            annlib_adaptbx/self_include/ANN.cpp
            annlib_adaptbx/self_include/bd_fix_rad_search.cpp
            annlib_adaptbx/self_include/bd_pr_search.cpp
            annlib_adaptbx/self_include/bd_search.cpp
            annlib_adaptbx/self_include/bd_tree.cpp
            annlib_adaptbx/self_include/brute.cpp
            annlib_adaptbx/self_include/kd_dump.cpp
            annlib_adaptbx/self_include/kd_fix_rad_search.cpp
            annlib_adaptbx/self_include/kd_pr_search.cpp
            annlib_adaptbx/self_include/kd_search.cpp
            annlib_adaptbx/self_include/kd_split.cpp
            annlib_adaptbx/self_include/kd_tree.cpp
            annlib_adaptbx/self_include/kd_util.cpp
            annlib_adaptbx/self_include/perf.cpp )
target_link_libraries(ann annlib annlib_adaptbx scitbx)

