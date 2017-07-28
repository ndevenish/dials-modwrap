add_python_library ( smtbx_refinement_constraints_ext
            affine.cpp
            constraints_ext.cpp
            direction.cpp
            geometrical_hydrogens.cpp
            independent_scalar_parameters.cpp
            occupancy.cpp
            reparametrisation.cpp
            rigid.cpp
            same_group.cpp
            scatterer_parameters.cpp
            shared.cpp
            special_position.cpp
            symmetry_equivalent.cpp
            u_eq_dependent_u_iso.cpp
            u_iso_dependent_u_iso.cpp )
target_link_libraries(smtbx_refinement_constraints_ext cctbx smtbx_refinement_constraints scitbx_boost_python)

