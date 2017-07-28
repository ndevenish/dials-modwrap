add_python_library ( rstbx_bandpass_ext
            ext.cpp )
target_link_libraries(rstbx_bandpass_ext cctbx ann rstbx scitbx_boost_python)

