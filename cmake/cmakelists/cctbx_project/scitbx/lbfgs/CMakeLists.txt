add_python_library ( scitbx_lbfgs_ext
            ext.cpp )
add_generated_sources(scitbx_lbfgs_ext
            scitbx/lbfgs/lbfgs_fem.cpp )
target_link_libraries(scitbx_lbfgs_ext scitbx_boost_python fable)

# As target is entirely generated sources, manually toggle the generated property
set_source_files_properties("${CMAKE_BINARY_DIR}/scitbx/lbfgs/lbfgs_fem.cpp" PROPERTIES GENERATED TRUE)
set_source_files_properties("${CMAKE_BINARY_DIR}/scitbx/lbfgs/sdrive_fem.cpp" PROPERTIES GENERATED TRUE)
add_executable(sdrive_fem ${CMAKE_BINARY_DIR}/scitbx/lbfgs/lbfgs_fem.cpp ${CMAKE_BINARY_DIR}/scitbx/lbfgs/sdrive_fem.cpp)
target_link_libraries(sdrive_fem scitbx fable)

add_executable(tst_lbfgs tst_lbfgs.cpp)
add_test(NAME tst_lbfgs COMMAND tst_lbfgs)

