add_python_library ( rstbx_array_family_flex_ext
            ext.cpp
            flex_rstbx_arrays.cpp )
target_link_libraries(rstbx_array_family_flex_ext cctbx rstbx scitbx_boost_python)

