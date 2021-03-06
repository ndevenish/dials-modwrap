project(ccp4io)

add_library ( ccp4io 
            libccp4/ccp4/ccp4_array.c
            libccp4/ccp4/ccp4_parser.c
            libccp4/ccp4/ccp4_unitcell.c
            libccp4/ccp4/cmap_accessor.c
            libccp4/ccp4/cmap_close.c
            libccp4/ccp4/cmap_data.c
            libccp4/ccp4/cmap_header.c
            libccp4/ccp4/cmap_labels.c
            libccp4/ccp4/cmap_open.c
            libccp4/ccp4/cmap_skew.c
            libccp4/ccp4/cmap_stats.c
            libccp4/ccp4/cmap_symop.c
            libccp4/ccp4/cmtzlib.c
            libccp4/ccp4/cvecmat.c
            libccp4/ccp4/library_err.c
            libccp4/ccp4/library_file.c
            libccp4/ccp4/library_utils.c
            mmdb/hybrid_36.cpp
            mmdb/mmdb_atom.cpp
            mmdb/mmdb_bondmngr.cpp
            mmdb/mmdb_chain.cpp
            mmdb/mmdb_cifdefs.cpp
            mmdb/mmdb_coormngr.cpp
            mmdb/mmdb_cryst.cpp
            mmdb/mmdb_ficif.cpp
            mmdb/mmdb_io_file.cpp
            mmdb/mmdb_io_stream.cpp
            mmdb/mmdb_machine_.cpp
            mmdb/mmdb_manager.cpp
            mmdb/mmdb_mask.cpp
            mmdb/mmdb_math_.cpp
            mmdb/mmdb_math_align.cpp
            mmdb/mmdb_math_bfgsmin.cpp
            mmdb/mmdb_math_fft.cpp
            mmdb/mmdb_math_graph.cpp
            mmdb/mmdb_math_linalg.cpp
            mmdb/mmdb_math_rand.cpp
            mmdb/mmdb_mattype.cpp
            mmdb/mmdb_mmcif_.cpp
            mmdb/mmdb_model.cpp
            mmdb/mmdb_root.cpp
            mmdb/mmdb_rwbrook.cpp
            mmdb/mmdb_selmngr.cpp
            mmdb/mmdb_seqsuperpose.cpp
            mmdb/mmdb_symop.cpp
            mmdb/mmdb_tables.cpp
            mmdb/mmdb_title.cpp
            mmdb/mmdb_uddata.cpp
            mmdb/mmdb_utils.cpp
            mmdb/mmdb_xml_.cpp
            ssm/ssm_align.cpp
            ssm/ssm_csia.cpp
            ssm/ssm_graph.cpp
            ssm/ssm_malign.cpp
            ssm/ssm_superpose.cpp
            ssm/ssm_vxedge.cpp
            ../ccp4io_adaptbx/fortran_call_stubs.c
            ../ccp4io_adaptbx/printf_wrappers.c )
add_generated_sources(ccp4io
            ccp4io_adaptbx/ccp4_diskio_f.c
            ccp4io_adaptbx/ccp4_general.c
            ccp4io_adaptbx/ccp4_general_f.c
            ccp4io_adaptbx/ccp4_parser_f.c
            ccp4io_adaptbx/ccp4_program.c
            ccp4io_adaptbx/ccp4_unitcell_f.c
            ccp4io_adaptbx/cmaplib_f.c
            ccp4io_adaptbx/cmtzlib_f.c
            ccp4io_adaptbx/csymlib.c
            ccp4io_adaptbx/csymlib_f.c
            ccp4io_adaptbx/library_f.c )
target_link_libraries(ccp4io scitbx)
target_include_directories(ccp4io PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/. ${CMAKE_CURRENT_SOURCE_DIR}/libccp4/ccp4)


