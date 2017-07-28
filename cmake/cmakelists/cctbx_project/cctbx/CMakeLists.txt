project(cctbx)

add_library ( cctbx 
            eltbx/attenuation_coefficient.cpp
            eltbx/basic.cpp
            eltbx/covalent_radii.cpp
            eltbx/electron_scattering/peng1996.cpp
            eltbx/fp_fdp.cpp
            eltbx/icsd_radii.cpp
            eltbx/neutron.cpp
            eltbx/tiny_pse.cpp
            eltbx/wavelengths.cpp
            eltbx/xray_scattering/it1992.cpp
            eltbx/xray_scattering/n_gaussian.cpp
            eltbx/xray_scattering/n_gaussian_raw.cpp
            eltbx/xray_scattering/wk1995.cpp
            miller/asu.cpp
            miller/bins.cpp
            miller/index_generator.cpp
            miller/index_span.cpp
            miller/match_bijvoet_mates.cpp
            miller/match_indices.cpp
            miller/match_multi_indices.cpp
            miller/sym_equiv.cpp
            sgtbx/bricks.cpp
            sgtbx/change_of_basis_op.cpp
            sgtbx/find_affine.cpp
            sgtbx/group_codes.cpp
            sgtbx/hall_in.cpp
            sgtbx/lattice_tr.cpp
            sgtbx/lattice_symmetry.cpp
            sgtbx/miller.cpp
            sgtbx/reciprocal_space_asu.cpp
            sgtbx/reciprocal_space_ref_asu.cpp
            sgtbx/rot_mx.cpp
            sgtbx/rot_mx_info.cpp
            sgtbx/row_echelon_solve.cpp
            sgtbx/rt_mx.cpp
            sgtbx/select_generators.cpp
            sgtbx/seminvariant.cpp
            sgtbx/site_symmetry.cpp
            sgtbx/space_group.cpp
            sgtbx/space_group_type.cpp
            sgtbx/symbols.cpp
            sgtbx/tensor_rank_2.cpp
            sgtbx/tr_group.cpp
            sgtbx/tr_vec.cpp
            sgtbx/utils.cpp
            sgtbx/wyckoff.cpp
            sgtbx/reference_settings/hall_symbol_table.cpp
            sgtbx/reference_settings/matrix_group_code_table.cpp
            sgtbx/reference_settings/normalizer.cpp
            sgtbx/reference_settings/wyckoff.cpp
            uctbx/uctbx.cpp
            uctbx/spoil_optimization.cpp
            uctbx/crystal_orientation.cpp )
add_generated_sources(cctbx
            cctbx/eltbx/henke.cpp
            cctbx/eltbx/henke_tables_01_12.cpp
            cctbx/eltbx/henke_tables_13_24.cpp
            cctbx/eltbx/henke_tables_25_36.cpp
            cctbx/eltbx/henke_tables_37_48.cpp
            cctbx/eltbx/henke_tables_49_60.cpp
            cctbx/eltbx/henke_tables_61_72.cpp
            cctbx/eltbx/henke_tables_73_84.cpp
            cctbx/eltbx/henke_tables_85_92.cpp
            cctbx/eltbx/sasaki.cpp
            cctbx/eltbx/sasaki_tables_01_12.cpp
            cctbx/eltbx/sasaki_tables_13_24.cpp
            cctbx/eltbx/sasaki_tables_25_36.cpp
            cctbx/eltbx/sasaki_tables_37_48.cpp
            cctbx/eltbx/sasaki_tables_49_60.cpp
            cctbx/eltbx/sasaki_tables_61_72.cpp
            cctbx/eltbx/sasaki_tables_73_82.cpp )
target_link_libraries(cctbx Boost::boost)
target_include_directories(cctbx PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/${CMAKE_CURRENT_SOURCE_DIR}/..)


add_libtbx_refresh_command( ${CMAKE_CURRENT_SOURCE_DIR}/libtbx_refresh.py
     OUTPUT ${CMAKE_BINARY_DIR}/cctbx/eltbx/henke.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/henke_tables_01_12.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/henke_tables_13_24.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/henke_tables_25_36.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/henke_tables_37_48.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/henke_tables_49_60.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/henke_tables_61_72.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/henke_tables_73_84.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/henke_tables_85_92.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/sasaki.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/sasaki_tables_01_12.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/sasaki_tables_13_24.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/sasaki_tables_25_36.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/sasaki_tables_37_48.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/sasaki_tables_49_60.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/sasaki_tables_61_72.cpp
            ${CMAKE_BINARY_DIR}/cctbx/eltbx/sasaki_tables_73_82.cpp
            ${CMAKE_BINARY_DIR}/include/cctbx/boost_python/flex_fwd.h )

add_subdirectory(adp_restraints)
add_subdirectory(adptbx)
add_subdirectory(array_family)
add_subdirectory(boost_python)
add_subdirectory(covariance)
add_subdirectory(crystal)
add_subdirectory(dmtbx)
add_subdirectory(eltbx)
add_subdirectory(examples)
add_subdirectory(geometry)
add_subdirectory(geometry_restraints)
add_subdirectory(maptbx)
add_subdirectory(masks)
add_subdirectory(math)
add_subdirectory(merging)
add_subdirectory(miller)
add_subdirectory(multipolar)
add_subdirectory(sgtbx)
add_subdirectory(symmetry_search)
add_subdirectory(translation_search)
add_subdirectory(uctbx)
add_subdirectory(xray)
