add_python_library ( rstbx_simage_ext
            ext.cpp )
target_link_libraries(rstbx_simage_ext cctbx rstbx scitbx_boost_python)

