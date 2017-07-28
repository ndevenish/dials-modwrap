add_executable(cctbx.convert_ccp4_symop_lib convert_ccp4_symop_lib.cpp)
set_target_properties(cctbx.convert_ccp4_symop_lib PROPERTIES     RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/exe_dev)
target_link_libraries(cctbx.convert_ccp4_symop_lib cctbx cctbx_sgtbx_asu)

add_executable(cctbx.find_distances find_distances.cpp)
set_target_properties(cctbx.find_distances PROPERTIES     RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/exe_dev)
target_link_libraries(cctbx.find_distances cctbx cctbx_sgtbx_asu)

add_executable(cctbx.getting_started getting_started.cpp)
set_target_properties(cctbx.getting_started PROPERTIES     RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/exe_dev)
target_link_libraries(cctbx.getting_started cctbx cctbx_sgtbx_asu)

add_executable(cctbx.lattice_symmetry lattice_symmetry.cpp)
set_target_properties(cctbx.lattice_symmetry PROPERTIES     RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/exe_dev)
target_link_libraries(cctbx.lattice_symmetry cctbx cctbx_sgtbx_asu)

add_executable(cctbx.sym_equiv_sites sym_equiv_sites.cpp)
set_target_properties(cctbx.sym_equiv_sites PROPERTIES     RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/exe_dev)
target_link_libraries(cctbx.sym_equiv_sites cctbx cctbx_sgtbx_asu)

add_executable(cctbx.sys_abs_equiv_space_groups sys_abs_equiv_space_groups.cpp)
set_target_properties(cctbx.sys_abs_equiv_space_groups PROPERTIES     RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/exe_dev)
target_link_libraries(cctbx.sys_abs_equiv_space_groups cctbx cctbx_sgtbx_asu)

add_subdirectory(merging)
