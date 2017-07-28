add_python_library ( cctbx_adp_restraints_ext
            adp_restraints_bpl.cpp
            adp_restraints_ext.cpp
            adp_similarity_bpl.cpp
            aniso_restraints_bpl.cpp
            fixed_u_eq_adp_bpl.cpp
            isotropic_adp_bpl.cpp
            rigid_bond_bpl.cpp )
target_link_libraries(cctbx_adp_restraints_ext cctbx scitbx_boost_python)

