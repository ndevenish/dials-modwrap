add_python_library ( iotbx_cif_ext
            ucif/antlr3/src/antlr3baserecognizer.c
            ucif/antlr3/src/antlr3basetree.c
            ucif/antlr3/src/antlr3basetreeadaptor.c
            ucif/antlr3/src/antlr3bitset.c
            ucif/antlr3/src/antlr3collections.c
            ucif/antlr3/src/antlr3commontoken.c
            ucif/antlr3/src/antlr3commontree.c
            ucif/antlr3/src/antlr3commontreeadaptor.c
            ucif/antlr3/src/antlr3commontreenodestream.c
            ucif/antlr3/src/antlr3convertutf.c
            ucif/antlr3/src/antlr3cyclicdfa.c
            ucif/antlr3/src/antlr3debughandlers.c
            ucif/antlr3/src/antlr3encodings.c
            ucif/antlr3/src/antlr3exception.c
            ucif/antlr3/src/antlr3filestream.c
            ucif/antlr3/src/antlr3inputstream.c
            ucif/antlr3/src/antlr3intstream.c
            ucif/antlr3/src/antlr3lexer.c
            ucif/antlr3/src/antlr3parser.c
            ucif/antlr3/src/antlr3rewritestreams.c
            ucif/antlr3/src/antlr3string.c
            ucif/antlr3/src/antlr3tokenstream.c
            ucif/antlr3/src/antlr3treeparser.c
            iotbx/cif/boost_python/cif_ext.cpp
            ucif/cifParser.cpp
            ucif/cifLexer.cpp )
target_include_directories(iotbx_cif_ext PUBLIC ${CMAKE_SOURCE_DIR}/cctbx_project/ucif/antlr3/include ${CMAKE_SOURCE_DIR}/cctbx_project/ucif/antlr3)


add_subdirectory(boost_adaptbx)
add_subdirectory(cbflib_adaptbx)
add_subdirectory(cctbx)
add_subdirectory(chiltbx)
add_subdirectory(cma_es)
add_subdirectory(dxtbx)
add_subdirectory(fable)
add_subdirectory(gltbx)
add_subdirectory(iotbx)
add_subdirectory(mmtbx)
add_subdirectory(omptbx)
add_subdirectory(prime)
add_subdirectory(rstbx)
add_subdirectory(scitbx)
add_subdirectory(simtbx)
add_subdirectory(smtbx)
add_subdirectory(spotfinder)
add_subdirectory(xfel)
