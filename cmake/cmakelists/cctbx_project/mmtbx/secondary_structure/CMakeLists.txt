add_python_library ( mmtbx_dssp_ext
            dssp_ext.cpp )
target_link_libraries(mmtbx_dssp_ext iotbx_pdb cctbx scitbx_boost_python)

add_python_library ( mmtbx_secondary_structure_ext
            ext.cpp )
target_link_libraries(mmtbx_secondary_structure_ext iotbx_pdb cctbx scitbx_boost_python)

