project(mmtbx)

add_library( mmtbx INTERFACE )
target_include_directories(mmtbx INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_python_library ( mmtbx_alignment_ext
            alignment_ext.cpp )
target_link_libraries(mmtbx_alignment_ext scitbx_boost_python)

add_subdirectory(building)
add_subdirectory(bulk_solvent)
add_subdirectory(cablam)
add_subdirectory(den)
add_subdirectory(dynamics)
add_subdirectory(f_model)
add_subdirectory(geometry)
add_subdirectory(geometry_restraints)
add_subdirectory(hydrogens)
add_subdirectory(masks)
add_subdirectory(max_lik)
add_subdirectory(ncs)
add_subdirectory(rotamer)
add_subdirectory(rsr)
add_subdirectory(scaling)
add_subdirectory(secondary_structure)
add_subdirectory(tls)
add_subdirectory(utils)
add_subdirectory(validation)
