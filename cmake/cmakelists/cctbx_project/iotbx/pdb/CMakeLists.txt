add_library ( iotbx_pdb 
            hybrid_36_c.c
            hybrid_36_cpp.cpp
            utils.cpp
            write_utils.cpp
            hierarchy.cpp
            hierarchy_select.cpp
            hierarchy_atoms.cpp
            construct_hierarchy.cpp
            overall_counts.cpp
            hierarchy_write.cpp
            atom_selection.cpp
            input.cpp
            input_write.cpp )
target_link_libraries(iotbx_pdb iotbx)

add_python_library ( iotbx_pdb_ext
            ext.cpp
            hybrid_36_bpl.cpp
            common_residue_names_bpl.cpp
            rna_dna_atom_names_bpl.cpp
            input_bpl.cpp
            xray_structure_bpl.cpp )
target_link_libraries(iotbx_pdb_ext iotbx_pdb cctbx scitbx_boost_python)

add_python_library ( iotbx_pdb_hierarchy_ext
            hierarchy_ext.cpp
            hierarchy_atom_bpl.cpp
            hierarchy_atoms_bpl.cpp )
target_link_libraries(iotbx_pdb_hierarchy_ext iotbx_pdb cctbx scitbx_boost_python)

# As target is entirely generated sources, manually toggle the generated property
set_source_files_properties("${CMAKE_BINARY_DIR}/iotbx/pdb/hybrid_36_fem.cpp" PROPERTIES GENERATED TRUE)
add_executable(hybrid_36_fem ${CMAKE_BINARY_DIR}/iotbx/pdb/hybrid_36_fem.cpp)
target_link_libraries(hybrid_36_fem iotbx fable)

