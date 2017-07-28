add_python_library ( dials_algorithms_integration_ext
            corrections.cc
            integration_ext.cc )
target_link_libraries(dials_algorithms_integration_ext cctbx scitbx_boost_python)

add_python_library ( dials_algorithms_integration_integrator_ext
            integration_integrator_ext.cc )
target_link_libraries(dials_algorithms_integration_integrator_ext cctbx scitbx_boost_python)

