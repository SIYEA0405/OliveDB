import Head from "next/head";
import { CSSReset, VStack, Box, Flex } from "@chakra-ui/react";
import Header from "./Header";
import Footer from "./Footer";
import { ReactNode } from "react";

interface LayoutProps {
  children: ReactNode;
}

const Layout = ({ children }: LayoutProps) => {
  return (
    <>
      <Head>
        <title>OliveDB</title>
        <meta
          name="description"
          content="OliveDB is database of everything on Oliveyoung."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/oliveDB_logo.ico" />
      </Head>
      <CSSReset />
      <VStack spacing={0} align="stretch" minH="100vh" bg="bodyBg">
        <Header flex="2" />
        <Box as="main" p="10%" flex="8" alignContent="center">
          <Flex
            flexDirection="column"
            justifyContent="center"
            alignItems="center"
          >
            {children}
          </Flex>
        </Box>
        <Footer />
      </VStack>
    </>
  );
};

export default Layout;
