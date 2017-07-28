add_python_library ( dials_scaling_helpers_ext
            obs_manager_helpers.cc
            scale_parameterisation_helpers.cc
            scaling_ext.cc )
target_link_libraries(dials_scaling_helpers_ext cctbx scitbx_boost_python)

