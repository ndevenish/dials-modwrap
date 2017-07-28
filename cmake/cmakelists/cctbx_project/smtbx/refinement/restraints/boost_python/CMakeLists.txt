add_python_library ( smtbx_refinement_restraints_ext
            origin_fixing.cpp
            restraints_ext.cpp )
target_link_libraries(smtbx_refinement_restraints_ext cctbx)

