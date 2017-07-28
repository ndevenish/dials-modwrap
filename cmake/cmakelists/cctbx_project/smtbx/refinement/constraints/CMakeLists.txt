add_library ( smtbx_refinement_constraints 
            affine.cpp
            geometrical_hydrogens.cpp
            occupancy.cpp
            reparametrisation.cpp
            rigid.cpp
            same_group.cpp
            shared.cpp
            special_position.cpp
            symmetry_equivalent.cpp
            u_eq_dependent_u_iso.cpp
            u_iso_dependent_u_iso.cpp )
target_link_libraries(smtbx_refinement_constraints smtbx)

add_subdirectory(boost_python)
add_subdirectory(tests)
