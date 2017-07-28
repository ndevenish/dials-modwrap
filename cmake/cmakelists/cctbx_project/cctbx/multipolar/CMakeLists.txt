add_python_library ( cctbx_multipolar_ext
            aspherical_ext.cpp )
target_link_libraries(cctbx_multipolar_ext cctbx scitbx_boost_python)

