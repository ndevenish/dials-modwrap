add_python_library ( mmtbx_ncs_ext
            tncs_ext.cpp )
target_link_libraries(mmtbx_ncs_ext cctbx scitbx_boost_python)

add_python_library ( mmtbx_ncs_restraints_ext
            restraints_ext.cpp )
target_link_libraries(mmtbx_ncs_restraints_ext cctbx scitbx_boost_python)

