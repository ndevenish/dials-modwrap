add_python_library ( cctbx_sgtbx_ext
            brick.cpp
            change_of_basis.cpp
            find_affine.cpp
            lattice_symmetry.cpp
            phase_info.cpp
            reciprocal_space_asu.cpp
            rot_mx.cpp
            rt_mx.cpp
            search_symmetry.cpp
            select_generators.cpp
            seminvariant.cpp
            sgtbx_ext.cpp
            site_symmetry.cpp
            space_group.cpp
            space_group_type.cpp
            sym_equiv_sites.cpp
            symbols.cpp
            tensor_rank_2.cpp
            tr_vec.cpp
            wyckoff.cpp )
target_link_libraries(cctbx_sgtbx_ext cctbx scitbx_boost_python)

