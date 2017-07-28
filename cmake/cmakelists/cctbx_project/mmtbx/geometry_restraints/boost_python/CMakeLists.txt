add_python_library ( mmtbx_ramachandran_restraints_ext
            ramachandran_ext.cpp )
target_link_libraries(mmtbx_ramachandran_restraints_ext cctbx scitbx_boost_python)

add_python_library ( mmtbx_reference_coordinate_ext
            reference_coordinate_ext.cpp )
target_link_libraries(mmtbx_reference_coordinate_ext cctbx scitbx_boost_python)

