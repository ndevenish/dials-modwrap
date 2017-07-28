add_python_library ( cctbx_crystal_ext
            asu_clusters_bpl.cpp
            close_packing_bpl.cpp
            coordination_sequences_bpl.cpp
            crystal_ext.cpp
            direct_space_asu_bpl.cpp
            incremental_pairs_bpl.cpp
            neighbors_bpl.cpp
            pair_tables_bpl.cpp
            site_cluster_analysis_bpl.cpp
            symmetry_bpl.cpp )
target_link_libraries(cctbx_crystal_ext cctbx scitbx_boost_python)

