add_python_library ( dials_algorithms_simulation_ext
            simulation_ext.cc )
target_link_libraries(dials_algorithms_simulation_ext cctbx scitbx_boost_python)

