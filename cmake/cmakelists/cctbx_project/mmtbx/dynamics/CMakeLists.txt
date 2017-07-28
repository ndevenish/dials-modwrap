add_python_library ( mmtbx_dynamics_ext
            dynamics_ext.cpp
            dynamics.cpp )
target_link_libraries(mmtbx_dynamics_ext cctbx scitbx_boost_python)

