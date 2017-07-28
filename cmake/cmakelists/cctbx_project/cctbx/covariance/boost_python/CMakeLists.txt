add_python_library ( cctbx_covariance_ext
            covariance_ext.cpp )
target_link_libraries(cctbx_covariance_ext cctbx scitbx_boost_python)

