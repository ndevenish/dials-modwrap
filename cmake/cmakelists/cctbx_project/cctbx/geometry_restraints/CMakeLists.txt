add_python_library ( cctbx_geometry_restraints_ext
            angle_bpl.cpp
            bond_bpl.cpp
            bond_similarity_bpl.cpp
            bond_sorted_bpl.cpp
            chirality_bpl.cpp
            dihedral_bpl.cpp
            geometry_restraints_ext.cpp
            motif_bpl.cpp
            nonbonded_bpl.cpp
            nonbonded_sorted_bpl.cpp
            parallelity_bpl.cpp
            planarity_bpl.cpp )
target_link_libraries(cctbx_geometry_restraints_ext cctbx scitbx_boost_python)

