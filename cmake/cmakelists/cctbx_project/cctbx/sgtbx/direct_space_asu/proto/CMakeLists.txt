add_library ( cctbx_sgtbx_asu 
            cut.cpp
            direct_space_asu.cpp
            reference_table.cpp )
target_link_libraries(cctbx_sgtbx_asu cctbx)

add_python_library ( cctbx_sgtbx_asu_ext
            asu_ext.cpp )
target_link_libraries(cctbx_sgtbx_asu_ext cctbx cctbx_sgtbx_asu scitbx_boost_python)

add_executable(tst_asu tst_asu.cpp)
target_link_libraries(tst_asu cctbx cctbx_sgtbx_asu)
add_test(NAME tst_asu COMMAND tst_asu)

