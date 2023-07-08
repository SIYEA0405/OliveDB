import { Flex, FlexProps } from "@chakra-ui/react";
interface FooterProps extends FlexProps {}
const Footer: React.FC<FooterProps> = (props) => {
  return (
    <>
      <Flex bg="gray" {...props}>
        Footer
      </Flex>
    </>
  );
};

export default Footer;
