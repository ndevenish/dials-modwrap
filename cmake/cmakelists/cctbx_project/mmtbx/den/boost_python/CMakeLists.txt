add_python_library ( mmtbx_den_restraints_ext
            den_ext.cpp )
target_link_libraries(mmtbx_den_restraints_ext cctbx scitbx_boost_python)

