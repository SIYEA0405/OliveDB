import { CSSReset, VStack, Box } from "@chakra-ui/react";
import Header from "./Header"
import Footer from "./Footer";
import { ReactNode } from "react";

interface LayoutProps {
  children: ReactNode;
}

const Layout = ({ children }: LayoutProps) => {
  return (
    <>
      <CSSReset />
      <VStack spacing={0} align="stretch" h="100vh" bg="#F2F2F2">
        <Header flex="2" />
        <Box as="main" flex="5.5">
          {children}
        </Box>
        <Footer flex="1.5"/>
      </VStack>
    </>
  );
};

export default Layout;
