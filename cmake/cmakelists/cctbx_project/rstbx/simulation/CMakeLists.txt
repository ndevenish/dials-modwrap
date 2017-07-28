add_python_library ( rstbx_simulation_ext
            ext.cpp )
target_link_libraries(rstbx_simulation_ext cctbx rstbx scitbx_boost_python)

