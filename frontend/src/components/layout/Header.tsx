import Link from "next/link";
import { Flex, FlexProps, Heading, Text } from "@chakra-ui/react";
interface HeaderProps extends FlexProps {}

const Header: React.FC<HeaderProps> = (props) => {
  return (
    <>
      <Flex justify="center" align="center" {...props} pt="5%">
        <Link href="/">
          <Heading as="h1" size="4xl">
            <Flex>
              <Text color="#BBD94E">O</Text>
              <Text>live</Text>
              <Text color="#F27D72">DB</Text>
            </Flex>
          </Heading>
        </Link>
      </Flex>
    </>
  );
};
export default Header;
