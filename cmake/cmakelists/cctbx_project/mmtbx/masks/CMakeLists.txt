add_library ( mmtbx_masks 
            atom_mask.cpp )
target_link_libraries(mmtbx_masks mmtbx cctbx_sgtbx_asu omptbx cctbx)

add_python_library ( mmtbx_masks_ext
            masks_ext.cpp )
target_link_libraries(mmtbx_masks_ext cctbx cctbx_sgtbx_asu omptbx mmtbx_masks scitbx_boost_python)

add_executable(tst_mask tst_mask.cpp)
target_link_libraries(tst_mask iotbx_pdb cctbx cctbx_sgtbx_asu omptbx mmtbx_masks)
add_test(NAME tst_mask COMMAND tst_mask)

