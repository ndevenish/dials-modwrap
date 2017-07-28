add_python_library ( rstbx_integration_ext
            integration_ext.cpp )
target_link_libraries(rstbx_integration_ext cctbx ann rstbx spotfinder scitbx_boost_python)

